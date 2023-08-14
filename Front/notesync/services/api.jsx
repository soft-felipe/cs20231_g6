"use client"

import axios from "axios";

const api = axios.create({
  baseURL: "http://18.233.10.135/",
});

export async function fetchTodos() {
  try {
    const response = await axios.get('http://your-api-endpoint.com/todos');
    return response.data;
  } catch (error) {
    throw new Error('Error fetching data:', error);
  }
}



export default api;