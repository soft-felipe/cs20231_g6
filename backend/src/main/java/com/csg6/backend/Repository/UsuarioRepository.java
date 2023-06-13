package com.csg6.backend.Repository;

import com.csg6.backend.Model.Usuario;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
    Usuario findByUsernameOrEmail(String username, String email);

}
