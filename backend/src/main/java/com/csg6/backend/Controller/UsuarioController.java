package com.csg6.backend.Controller;

import com.csg6.backend.Model.Usuario;
import com.csg6.backend.Service.UsuarioService;
import lombok.RequiredArgsConstructor;

import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import java.util.List;

@Controller
@RequestMapping("/usuario")
@RequiredArgsConstructor
public class UsuarioController {
    private final UsuarioService usuarioService;

    @GetMapping(value = "/listar", produces = MediaType.APPLICATION_JSON_VALUE)
    protected ResponseEntity<List<Usuario>> listar(){
        return ResponseEntity.ok(usuarioService.listar());
    }

    @DeleteMapping(value = "/deletar", produces = MediaType.APPLICATION_JSON_VALUE)
    protected ResponseEntity<String> deletar(@RequestBody Usuario usuario){
        try{
            usuarioService.deletar(usuario);
        }
        catch(Exception e){
            return ResponseEntity.badRequest().body(e.getMessage());
        }
        return ResponseEntity.ok().body("Sucesso!");
    }


}
