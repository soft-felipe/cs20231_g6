import Header from '@/components/Header'
import Board from '@/components/Board'
import Board2 from '@/components/Board2'

function Dashboard() {
  return (
    <main className="flex  min-h-screen flex-col bg-neutral-900">
    <Header />
      <div>
        <Board2/>
      </div>
    </main>
  )
}

export default Dashboard
