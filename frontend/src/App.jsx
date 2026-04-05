import React, { useState } from 'react';
import { predictPCB } from './services/api';
import UploadBox from './components/UploadBox';
import ResultDisplay from './components/ResultDisplay';
import { Cpu, ShieldCheck, Activity, Box } from 'lucide-react';
import { motion } from 'framer-motion'; // For smooth animations

function App() {
  const [resultImage, setResultImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileUpload = async (file) => {
    setLoading(true);
    setError(null);
    try {
      const data = await predictPCB(file);
      setResultImage(data.image_with_bounding_boxes);
    } catch (err) {
      setError("Server connection failed. Please ensure FastAPI is active.");
    } finally {
      setLoading(false);
    }
  };

  return (
    // Background: Deep Slate to Navy Gradient
    <div className="min-h-screen bg-gradient-to-br from-[#0f172a] via-[#1e293b] to-[#0f172a] text-slate-200 py-10 px-4">
      
      {/* Decorative Background Elements */}
      <div className="fixed top-0 left-0 w-full h-full overflow-hidden pointer-events-none opacity-20">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-blue-500 rounded-full blur-[120px]"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-indigo-600 rounded-full blur-[120px]"></div>
      </div>

      <div className="max-w-6xl mx-auto relative z-10">
        {/* Header Section */}
        <header className="flex flex-col items-center mb-16">
          <motion.div 
            initial={{ scale: 0 }} animate={{ scale: 1 }}
            className="bg-blue-500/20 p-4 rounded-2xl border border-blue-400/30 shadow-[0_0_20px_rgba(59,130,246,0.3)] mb-6"
          >
            <Cpu size={48} className="text-blue-400" />
          </motion.div>
          <h1 className="text-5xl font-black bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-300 tracking-tighter mb-2">
            PCB Defect Detection by Rakib
          </h1>
          <div className="flex items-center gap-4 text-slate-400 font-medium tracking-wide">
            <span className="flex items-center gap-1"><ShieldCheck size={16}/> Quality Assurance</span>
            <span className="w-1 h-1 bg-slate-600 rounded-full"></span>
            <span className="flex items-center gap-1"><Activity size={16}/> Real-time Inference</span>
          </div>
        </header>

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Left Side: Stats & Info (Recruiters love details) */}
          <div className="lg:col-span-4 space-y-6">
            <div className="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <h3 className="text-blue-400 font-bold uppercase text-xs tracking-widest mb-4">System Status</h3>
              <div className="space-y-4">
                <StatusItem label="Model" value="YOLOv11n" icon={<Box size={16}/>}/>
                <StatusItem label="Confidence" value="0.25 Threshold" icon={<Activity size={16}/>}/>
                <StatusItem label="Input Size" value="640x640px" icon={<Cpu size={16}/>}/>
              </div>
            </div>
            
            <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-6 rounded-2xl shadow-xl">
              <h3 className="text-white font-bold mb-2">Ready to Inspect?</h3>
              <p className="text-blue-100 text-sm">Upload a high-res PCB image to identify defects like missing_hole, mouse_bite, open_circuit, short, spur and spurious_copper instantly.</p>
            </div>
          </div>

          {/* Right Side: Upload & Results */}
          <div className="lg:col-span-8 flex flex-col items-center">
            <UploadBox onUpload={handleFileUpload} loading={loading} isDark />
            
            {error && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mt-4 p-4 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl w-full text-center">
                {error}
              </motion.div>
            )}

            <ResultDisplay base64Image={resultImage} />
          </div>
        </div>
      </div>
    </div>
  );
}

// Helper component for the sidebar
const StatusItem = ({ label, value, icon }) => (
  <div className="flex items-center justify-between">
    <div className="flex items-center gap-3 text-slate-400">
      {icon} <span className="text-sm font-medium">{label}</span>
    </div>
    <span className="text-sm text-slate-200 font-mono">{value}</span>
  </div>
);

export default App;