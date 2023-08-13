import Header from '@/components/Header'
import Board from '@/components/Board'

function Dashboard() {
  return (
    <main className="flex  min-h-screen flex-col bg-neutral-900">
    <Header />
      <div>
        <Board/>
      </div>
    </main>
  )
}

export default Dashboard
