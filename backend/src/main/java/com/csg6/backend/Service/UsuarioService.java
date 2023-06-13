package com.csg6.backend.Service;

import com.csg6.backend.Model.Usuario;
import com.csg6.backend.Repository.UsuarioRepository;
import com.csg6.backend.Service.Interface.UsuarioServiceInterface;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class UsuarioService implements UsuarioServiceInterface {
    @Autowired
    private UsuarioRepository usuarioRepository;

    @Transactional(propagation = Propagation.SUPPORTS, isolation = Isolation.READ_COMMITTED, timeout = 60)
    public List<Usuario> listar() {
        return usuarioRepository.findAll();
    }

    @Transactional(propagation = Propagation.REQUIRED, isolation = Isolation.READ_COMMITTED, rollbackFor = java.lang.Exception.class, timeout = 60)
    public Usuario registrar(Usuario usuario) {
        Usuario u = null;

        try{
            if(usuarioRepository.findByUsernameOrEmail(usuario.getUsername(), usuario.getEmail()) == null){
                u = usuarioRepository.save(usuario);
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }

        return u;
    }



}
