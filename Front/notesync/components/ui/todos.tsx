import React from 'react'
import { DragDropContext, Draggable, Droppable } from 'react-beautiful-dnd'
import { Status, Todo, TodosStatus, TodosView } from './todo'
import TodoItem from './todoItem'

interface Props {
  view: TodosView
  backlogTodos: Todo[]
  setBacklogTodos: React.Dispatch<React.SetStateAction<Todo[]>>
  activeTodos: Todo[]
  setActiveTodos: React.Dispatch<React.SetStateAction<Todo[]>>
  completedTodos: Todo[]
  setCompletedTodos: React.Dispatch<React.SetStateAction<Todo[]>>
}

const Todos: React.FC<Props> = ({
  view,
  backlogTodos,
  setBacklogTodos,
  activeTodos,
  setActiveTodos,
  completedTodos,
  setCompletedTodos,
}) => (
  view === TodosView.KanbanView ?
    <div className='grid grid-cols-1 w-full gap-6 mt-4 lg:grid-cols-3'>
      <Droppable droppableId={TodosStatus.BacklogTodos}>
        {
          (droppableProvided, droppableSnapshot) => (
            <div className='bg-gray-400 px-5 py-3 rounded-md'
              ref={droppableProvided.innerRef}
              {...droppableProvided.droppableProps}
            >
              <span className='text-white text-2xl font-semibold'>
                Backlog
              </span>
              {backlogTodos?.map((todo, index) =>
                <TodoItem
                  hasDoneIcon={false}
                  index={index}
                  key={todo?.id}
                  todo={todo}
                  todos={backlogTodos}
                  setTodos={setBacklogTodos} />
              )}
              {droppableProvided.placeholder}
            </div>
          )}
      </Droppable>
      <Droppable droppableId={TodosStatus.ActiveTodos}>
        {
          (droppableProvided, droppableSnapshot) => (
            <div className={`bg-blue-400 px-5 py-3 rounded-md ${droppableSnapshot.isDraggingOver ? 'opacity-80' : ''}`}
              ref={droppableProvided.innerRef}
              {...droppableProvided.droppableProps}
            >
              <span className='text-white text-2xl font-semibold'>
                Active
              </span>
              {activeTodos?.map((todo, index) =>
                <TodoItem
                  hasDoneIcon={false}
                  index={index}
                  key={todo?.id}
                  todo={todo}
                  todos={activeTodos}
                  setTodos={setActiveTodos}
                />
              )}
              {droppableProvided.placeholder}
            </div>
          )}
      </Droppable>
      <Droppable droppableId={TodosStatus.CompletedTodos}>
        {
          (droppableProvided, droppableSnapshot) => (
            <div className='bg-red-400 px-5 py-3 rounded-md'
              ref={droppableProvided.innerRef}
              {...droppableProvided.droppableProps}
            >
              <span className='text-white text-2xl font-semibold'>
                Completed
              </span>
              {completedTodos?.map((todo, index) =>
                <TodoItem
                  hasDoneIcon={false}
                  index={index}
                  key={todo.id}
                  todo={todo}
                  todos={completedTodos}
                  setTodos={setCompletedTodos}
                />
              )}
              {droppableProvided.placeholder}
            </div>
          )}
      </Droppable>
    </div>
    :
    <div className='grid grid-cols-1 w-full gap-2 mt-4 lg:grid-cols-5'> 
    </div>
)

export default Todos