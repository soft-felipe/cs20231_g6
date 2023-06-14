package com.csg6.backend.Service;

import com.csg6.backend.Exception.DAOException;
import com.csg6.backend.Model.Usuario;
import com.csg6.backend.Repository.UsuarioRepository;

import lombok.RequiredArgsConstructor;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class UsuarioService {
    
    private final UsuarioRepository usuarioRepository;

    @Transactional(propagation = Propagation.SUPPORTS, isolation = Isolation.READ_COMMITTED, timeout = 60)
    public List<Usuario> listar() {
        return usuarioRepository.findAll();
    }
   
    @Transactional(propagation = Propagation.REQUIRED, isolation = Isolation.READ_COMMITTED, rollbackFor = java.lang.Exception.class, timeout = 60)
    public void deletar(Usuario usuario){
        try{
            usuarioRepository.deleteById(usuario.getId());
        }
        catch(Exception e){
            e.printStackTrace();
            throw new DAOException("Erro ao deletar usuário");
        }
    }

}
