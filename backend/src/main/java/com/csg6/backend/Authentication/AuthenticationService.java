package com.csg6.backend.Authentication;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import com.csg6.backend.Config.JwtService;
import com.csg6.backend.Exception.DAOException;
import com.csg6.backend.Model.Role;
import com.csg6.backend.Model.Usuario;
import com.csg6.backend.Repository.UsuarioRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class AuthenticationService {

    private final UsuarioRepository repository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    
    public AuthenticationResponse register(RegisterRequest request) {
        var usuario = Usuario.builder()
        .username(request.getUsername())
        .email(request.getEmail())
        .senha(passwordEncoder.encode(request.getSenha()))
        .role(Role.USER)
        .build();

        //todo verificacoes no bd
        repository.save(usuario);
        var jwtToken = jwtService.generateToken(usuario);
        return AuthenticationResponse.builder().token(jwtToken).build();
    }

    public AuthenticationResponse authenticate(AuthenticationRequest request){
        authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(request.getUsername(), request.getSenha()));
        var usuario = repository.findByUsername(request.getUsername()).orElseThrow(() -> new DAOException());
        var jwtToken = jwtService.generateToken(usuario);
        return AuthenticationResponse.builder().token(jwtToken).build();
    }
    
}
