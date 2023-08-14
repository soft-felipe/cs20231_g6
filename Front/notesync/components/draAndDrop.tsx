import dynamic from 'next/dynamic'

const DragDropContext = dynamic(
  async () => {
    const mod = await import('react-beautiful-dnd')
    return mod.DragDropContext
  },
  { ssr: false }
)

const Droppable = dynamic(
  async () => {
    const mod = await import('react-beautiful-dnd')
    return mod.Droppable
  },
  { ssr: false }
)

const Draggable = dynamic(
  async () => {
    const mod = await import('react-beautiful-dnd')
    return mod.Draggable
  },
  { ssr: false }
)

export { DragDropContext, Droppable, Draggable}