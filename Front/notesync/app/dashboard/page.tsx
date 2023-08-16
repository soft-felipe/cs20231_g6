"use client"

import { TableDemo } from '@/components/DemoTable';
import Header from '@/components/Header'
import ProjectsTable from '@/components/projects/ProjectsTable';
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
      <div className='mx-40 my-10'>
          <div className='flex flex-col justify-between mb-12'>
            <div className='flex flex-col justify-between h-full my-10'>
                <div className='text-white font-extrabold text-2xl'>My Projects</div> 
            </div>
            <div>
            <TableDemo/>
            </div>  
          </div>
        </div>
    </main>
  )
}

export default Dashboard
