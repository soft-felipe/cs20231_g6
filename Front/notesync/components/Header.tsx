"use client"

import Image from 'next/image'
import React from 'react'

import Link from "next/link"
 
import { cn } from "@/lib/utils"

import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
  navigationMenuTriggerStyle
} from "@/components/ui/navigation-menu"


function Header() {
  return (
    <header>
      <div className='flex flex-col md:flex-row items-center p-4 bg-neutral-900'>
        <Image
          src="/logo.png"
          alt="NoteSync"
          width={300}
          height={100}
          className='w-44 md:w-56 pb-10 md:pb-0 object-contain'
        />
        <NavigationMenu>
          <NavigationMenuList>
          <NavigationMenuItem>
            <Link href="/projects" legacyBehavior passHref>
              <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                Projects
              </NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
      </div>
      
    </header>
  )
}

export default Header