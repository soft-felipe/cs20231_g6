package com.csg6.backend.Controller;

import com.csg6.backend.Model.Usuario;
import com.csg6.backend.Service.Interface.UsuarioServiceInterface;
import com.csg6.backend.Service.UsuarioService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
@RequestMapping("/usuario")
public class UsuarioController {

    @Autowired
    private UsuarioServiceInterface usuarioService;


    @GetMapping(value = "/listar", produces = MediaType.APPLICATION_JSON_VALUE)
    protected ResponseEntity<List<Usuario>> listar(){
        return ResponseEntity.ok(usuarioService.listar());
    }

    @PostMapping(value = "/registrar", produces = MediaType.APPLICATION_JSON_VALUE)
    protected ResponseEntity<Usuario> registrar(@RequestBody Usuario usuario){
       //todo
        return null;
    }
}
