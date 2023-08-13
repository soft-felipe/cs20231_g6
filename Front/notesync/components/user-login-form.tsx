"use client"

import * as React from "react"

import { cn } from "@/lib/utils"
import { Icons } from "@/components/Icons"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import api from "../services/api";

interface UserAuthFormProps extends React.HTMLAttributes<HTMLDivElement> {}

export function UserLoginForm({ className, ...props }: UserAuthFormProps) {
  const [isLoading, setIsLoading] = React.useState<boolean>(false)
  const [user, setUser] = React.useState(null)

  const baseURL = 'http://18.233.10.135'

  const handleSubmit = async e => {
    setIsLoading(true);
    e.preventDefault();

    const usernameInput = document.getElementById("username") as HTMLInputElement;
    const senhaInput = document.getElementById("senha") as HTMLInputElement;
    const emailInput = document.getElementById("email") as HTMLInputElement;

    const requestBody = {
      username: usernameInput.value,
      senha: senhaInput.value,
      email: emailInput.value,
  };
    // enviar o nome de usuário e a senha ao servidor
    const response = await api.post(
      `${baseURL}/usuario/login`,
      requestBody
    );
    // definir o state do usuário
    setUser(response.data)
    // armazenar o usuário em localStorage
    localStorage.setItem('user', response.data)
    console.log(response.data)
  };

  async function onSubmit(event: React.SyntheticEvent) {
    event.preventDefault();
    setIsLoading(true);
  
    const usernameInput = document.getElementById("username") as HTMLInputElement;
    const senhaInput = document.getElementById("senha") as HTMLInputElement;
    const emailInput = document.getElementById("email") as HTMLInputElement;

    const requestBody = {
        username: usernameInput.value,
        senha: senhaInput.value,
        email: emailInput.value,
    };
    
    console.log(requestBody);

    api.post(`${baseURL}/usuario/login`,requestBody
    )
      .then((response) => setIsLoading(false)) //
      .catch((err) => {
        console.error("Erro ao logar o usuário!" + err);
      });
    }
  return (
    <div className={cn("grid gap-6", className)} {...props}>
      <form onSubmit={onSubmit}>
        <div className="grid gap-2">
          <div className="grid gap-1">
            <Label className="sr-only" htmlFor="email">
              Email
            </Label>
            <Input
              id="email"
              placeholder="Email Address"
              type="text"
              autoCapitalize="none"
              autoComplete="email"
              autoCorrect="off"
              disabled={isLoading}
            />
          </div>
          <div className="grid gap-1">
            <Label className="sr-only" htmlFor="username">
              User
            </Label>
            <Input
              id="username"
              placeholder="Username"
              type="text"
              autoCapitalize="none"
              autoComplete="username"
              autoCorrect="off"
              disabled={isLoading}
            />
          </div>
          <div className="grid gap-1">
            <Label className="sr-only" htmlFor="password">
              Password
            </Label>
            <Input
              id="senha"
              placeholder="não sendo 123...ta valendo"
              type="password"
              autoCapitalize="none"
              autoComplete="senha"
              autoCorrect="off"
              disabled={isLoading}
            />
          </div>
          <Button disabled={isLoading} onClick={handleSubmit}>
            {isLoading && (
              <Icons.spinner className="mr-2 h-4 w-4 animate-spin" />
            )}
            Login
          </Button>
        </div>
      </form>
      <div className="relative">
        <div className="absolute inset-0 flex items-center">
          <span className="w-full border-t" />
        </div>
      </div>
    </div>
  )
}