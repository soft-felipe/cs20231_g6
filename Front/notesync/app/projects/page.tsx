"use client"

import Board2 from '@/components/Board2'
import Header from '@/components/Header'
import React from 'react'
import { v4 as uuidv4 } from 'uuid';


const membersFromBackend = [
    { id: 0, apelido: "John" },
    { id: 10, apelido: "Lara" },
    { id: 20, apelido: "Thiago" },
    { id: 30, apelido: "Siclano" },
    { id: 40, apelido: "Mais um ai" }
  ];



function Projects() {
  return (
    <main className="flex  min-h-screen flex-col bg-neutral-900">
    <Header />
      <div className='h-full px-56 mx-20'>
        <div className='flex flex-row justify-between mb-12'>
            <div className='flex flex-col justify-between h-full'>
                <div className='text-white font-extrabold text-2xl'>Title of the project</div>
                <div className='text-white'>Description of the project</div>  
            </div>
            <div>
                <div className='text-white font-extrabold text-lg justify-start w-full'>Members</div>
                <div className='h-auto w-14 flex flex-row justify-end'>
                    {membersFromBackend.map(member => (
                        <div key={member.id} className={`flex flex-col z-${member.id} bg-neutral-400 border-4 border-neutral-700 h-14 w-14 p-4 items-center justify-center rounded-full font-bold`}>
                        {member.apelido.charAt(0)}
                        </div>
                    ))}
                </div>
            </div>  
        </div>
        <Board2/>
      </div>
    </main>
  )
}

export default Projects