package com.csg6.backend.Controller;

import com.csg6.backend.Model.Usuario;
import com.csg6.backend.Service.Interface.UsuarioServiceInterface;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
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

    //refazer para mensagem de erro
    @PostMapping(value = "/registrar", produces = MediaType.APPLICATION_JSON_VALUE)
    protected ResponseEntity registrar(@RequestBody Usuario usuario){
        Usuario u = usuarioService.registrar(usuario);
        if(u != null){
            URI uri = UriComponentsBuilder.fromPath("/registrar").buildAndExpand(u.getId()).toUri();
            return ResponseEntity.created(uri).body(u);
        } 
        
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Erro ao registrar usuário");
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
