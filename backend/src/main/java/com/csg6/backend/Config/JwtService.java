package com.csg6.backend.Config;

import java.security.Key;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;

@Service
public class JwtService{

    private static final String SECRET_KEY = "840E4B3F7B75A02A89370FE920C797B18AEFD8544B9F1D8041088BEA238F68D47D665E87D4ED39AF091EE86E310A25BE2CE3BCA17B6DB36D7A9DAEF2F7B1240A35840DD3EDC800C1EAF44471769CE8C795B63E610FC49B217CF34BDD1D2AB9DA6F1F9179BD1770F3668D789912C05AA7EBA0CA105A16053E7F4BFCBD42525C80F9012D6FD2D5DC5E1FB8D7C8FD0484B93FFEE6D0C7BC0D07F0D0B70386CF832AFADD28D68F900D50D3F23317FC5726E15637330949F1C67BD4E4BEC6A15745CB830D2D1C5FC2DBD5B875674D751ECC719F81217935E11970ACD9DE87C3EB8B45D85E03B0CCEFE5689056EADB850C5D40695501E67BCC0634E2023F1CA5D3991C";


    public String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    public <T> T extractClaim(String token, Function<Claims, T> claimResolver){
        final Claims claims = extractAllClaims(token);
        return claimResolver.apply(claims);
    }

    public String generateToken(Map<String, Object> extraClaims, UserDetails userDetails){
        return Jwts
        .builder()
        .setClaims(extraClaims)
        .setSubject(userDetails.getUsername())
        .setIssuedAt(new Date(System.currentTimeMillis()))
        .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60))
        .signWith(getSignInKey(), SignatureAlgorithm.HS512)
        .compact();
    }

    public String generateToken(UserDetails userDetails){
        return generateToken(new HashMap<>(), userDetails);
    }

    public boolean isTokenValid(String token, UserDetails userDetails){
        final String username = extractUsername(token);
        return (username.equals(userDetails.getUsername())) && !isTokenExpired(token);
    }

    private boolean isTokenExpired(String token){
        return extractExpiration(token).before(new Date());
    }

    private Date extractExpiration(String token){
        return extractClaim(token, Claims::getExpiration);
    }
    
    private Claims extractAllClaims(String token){
        return Jwts
        .parserBuilder()
        .setSigningKey(getSignInKey())
        .build()
        .parseClaimsJws(token)
        .getBody();
    }

    private Key getSignInKey() {
        byte[] keyBytes = Decoders.BASE64.decode(SECRET_KEY);
        return Keys.hmacShaKeyFor(keyBytes);
    }
}
