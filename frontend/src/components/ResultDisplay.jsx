import React from 'react'; // Import React
import { Download } from 'lucide-react'; // Import download icon

// Component receives the base64 image string as a prop
const ResultDisplay = ({ base64Image }) => {
  // If no image is provided, don't render anything
  if (!base64Image) return null;

  return (
    // Container for the result section
    <div className="mt-10 w-full max-w-4xl flex flex-col items-center">
      <div className="flex items-center justify-between w-full mb-4">
        {/* Header for the results */}
        <h2 className="text-2xl font-bold text-gray-800">Detection Results</h2>
        
        {/* Simple download link to save the processed image */}
        <a 
          href={`data:image/jpeg;base64,${base64Image}`} 
          download="pcb_defect_result.jpg"
          className="flex items-center gap-2 text-blue-600 hover:text-blue-800 font-medium"
        >
          <Download size={18} /> Download Result
        </a>
      </div>

      {/* The main result image with shadow and rounded corners */}
      <div className="relative border-4 border-white shadow-2xl rounded-lg overflow-hidden bg-gray-200">
        <img 
          // Set src to the base64 string provided by FastAPI
          src={`data:image/jpeg;base64,${base64Image}`} 
          alt="Detected PCB Defects" 
          className="max-w-full h-auto"
        />
      </div>
    </div>
  );
};

export default ResultDisplay;