package com.csg6.backend.Service.Interface;

import com.csg6.backend.Model.Usuario;

import java.util.List;

public interface UsuarioServiceInterface {
    public List<Usuario> listar();

    public Usuario registrar(Usuario usuario);
}
