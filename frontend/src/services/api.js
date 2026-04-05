import axios from 'axios'; // Import axios for HTTP requests

// Define the base URL for your local FastAPI server
const API_BASE_URL = import.meta.env.VITE_API_URL ||  'http://localhost:8000'; 

// Create an axios instance with default settings
const api = axios.create({
  baseURL: API_BASE_URL, // Set the base URL
});

/**
 * Sends an image file to the /predict/ endpoint
 * @param {File} file - The image file from the input
 */
export const predictPCB = async (file) => {
  // Create a FormData object to send multipart/form-data
  const formData = new FormData();
  // Append the file using the key 'file' as expected by the backend
  formData.append('file', file);

  try {
    // Send the POST request to the /predict/ endpoint
    const response = await api.post('/predict/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data', // Tell the server we are sending a file
      },
    });
    // Return the response data (message, results, and base64 image)
    return response.data;
  } catch (error) {
    // Log any errors to the console
    console.error("API Error:", error);
    // Throw the error so the UI can handle it
    throw error;
  }
};