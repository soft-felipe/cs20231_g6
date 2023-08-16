import { promises as fs } from "fs"
import path from "path"
import { Metadata } from "next"
import Image from "next/image"
import { z } from "zod"

import { columns } from "./columns"
import { DataTable } from "./data-table"
import { UserNav } from "./user-nav"
import { projectSchema } from "../data/project-schema"

export const metadata: Metadata = {
  title: "Projects",
  description: "A table of projects that the user created or is involved with",
}
const projects = [
  {
    "id": "TASK-8782",
    "title": "You can't compress the program without quantifying the open-source SSD pixel!",
    "status": "in progress",
    "label": "documentation",
    "priority": "medium"
  },
  {
    "id": "TASK-7878",
    "title": "Try to calculate the EXE feed, maybe it will index the multi-byte pixel!",
    "status": "backlog",
    "label": "documentation",
    "priority": "medium"
  },
  {
    "id": "TASK-7839",
    "title": "We need to bypass the neural TCP card!",
    "status": "todo",
    "label": "bug",
    "priority": "high"
  },
  {
    "id": "TASK-5562",
    "title": "The SAS interface is down, bypass the open-source pixel so we can back up the PNG bandwidth!",
    "status": "backlog",
    "label": "feature",
    "priority": "medium"
  }
]

//const projects = JSON.parse(data.toString())

export default function ProjectsTable() {
  return (
    <>
      <div className="md:hidden">
        <Image
          src="/examples/tasks-light.png"
          width={1280}
          height={998}
          alt="Playground"
          className="block dark:hidden"
        />
        <Image
          src="/examples/tasks-dark.png"
          width={1280}
          height={998}
          alt="Playground"
          className="hidden dark:block"
        />
      </div>
      <div className="hidden h-full flex-1 flex-col space-y-8 p-8 md:flex">
        <div className="flex items-center justify-between space-y-2">
          <div>
            <h2 className="text-2xl font-bold tracking-tight">Welcome back!</h2>
            <p className="text-muted-foreground">
              Here&apos;s a list of your tasks for this month!
            </p>
          </div>
          <div className="flex items-center space-x-2">
            <UserNav />
          </div>
        </div>
        <DataTable data={projects} columns={columns} />
      </div>
    </>
  )
}