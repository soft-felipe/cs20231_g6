import { z } from "zod"

// We're keeping a simple non-relational schema here.
// IRL, you will have a schema for your data models.
export const projectSchema = z.object({
  id_projeto: z.string(),
  nome_projeto: z.string(),
  status: z.string(),
  label: z.string(),
  priority: z.string(),
})

export type Project = z.infer<typeof projectSchema>