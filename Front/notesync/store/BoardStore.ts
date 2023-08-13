import { create } from 'zustand'

interface BoardState{
    board: Board;
    getBoard: (board: Board) => Board
}

const useBearStore = create((set) => ({
  board: 0,
  getBoard: (board: Board) => board
}))