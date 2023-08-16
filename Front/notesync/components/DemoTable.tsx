import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table"
  
  const projectsFromBackend = [
    { id_projeto: 0, nome_projeto: "John", email:"user1@gmail.com" },
    { id_projeto: 1, nome_projeto: "Doe", email:"user2@gmail.com" },
    { id_projeto: 2, nome_projeto: "Fulano", email:"user3@gmail.com" },
  ];
  
  export function TableDemo() {
    return (
      <Table>
        <TableCaption className="font-medium text-white">A list of your recent projects.</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px] font-medium text-white">ID</TableHead>
            <TableHead className="w-[100px] font-medium text-white">Nome do projeto</TableHead>
            <TableHead className="text-right font-medium text-white ">Email do criador</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {projectsFromBackend.map((projects) => (
            <TableRow key={projects.id_projeto}>
              <TableCell className="font-medium text-white">{projects.id_projeto}</TableCell>
              <TableCell className=" text-white">{projects.nome_projeto}</TableCell>
              <TableCell className="text-right text-white">{projects.email}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    )
  }
  