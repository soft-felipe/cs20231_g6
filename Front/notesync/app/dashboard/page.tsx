"use client"

import Header from '@/components/Header'
import Board from '@/components/Board'
import Board2 from '@/components/Board2'
import axios from 'axios';
import {useEffect, useState} from 'react';

function Dashboard() {

  const [projects, setProjects] = useState([]);

  const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VydGVzdDE0IiwiZXhwIjoxNjkyMDQ4NjQ2fQ.25fGBKcn_nkvnx0nFomppZa7CFce7zCUxL-b0vtCBSs';

  useEffect(() => {
    axios.request({
      headers: {
        Authorization: `Bearer ${token}`
      },
      method: "GET",
      url: `http://18.233.10.135/projeto/13/listar`
    }).then(response => {
      setProjects(response.data);
      console.log(response.data);
    });
  }, []);


  return (
    <main className="flex  min-h-screen flex-col bg-neutral-900">
    <Header />
      <div>
      <div className='flex flex-row justify-between mb-12'>
            <div className='flex flex-col justify-between h-full'>
                <div className='text-white font-extrabold text-2xl'>My Projects</div>
                <div className='text-white'>Description of the project</div>  
            </div>
            <div>
            <div className='h-auto w-14 flex flex-row justify-end'>
                    {projects.map(project => (
                        <div key={project.id_projeto} className={`flex flex-col  bg-neutral-400 border-4 border-neutral-700 h-14 w-14 p-4 items-center justify-center rounded-full font-bold`}>
                          {project.nome_projeto} {project.email}
                        </div>
                    ))}
                </div>
            </div>  
        </div>
      </div>
    </main>
  )
}

export default Dashboard
