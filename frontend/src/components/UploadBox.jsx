import React from 'react';
import { Upload, Image as ImageIcon, Loader2 } from 'lucide-react';
import { motion } from 'framer-motion';

const UploadBox = ({ onUpload, loading }) => {
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) onUpload(file);
  };

  return (
    <motion.div 
      whileHover={{ scale: 1.01 }}
      className="w-full p-10 border-2 border-dashed border-slate-700 rounded-3xl bg-slate-800/40 backdrop-blur-xl flex flex-col items-center justify-center transition-all hover:border-blue-500/50 group"
    >
      <div className="bg-slate-700/50 p-5 rounded-full mb-6 group-hover:bg-blue-500/10 transition-colors">
        {loading ? (
          <Loader2 className="w-10 h-10 text-blue-400 animate-spin" />
        ) : (
          <Upload className="w-10 h-10 text-slate-400 group-hover:text-blue-400" />
        )}
      </div>
      
      <h3 className="text-xl font-bold text-slate-100 mb-2">Source Image Analysis</h3>
      <p className="text-slate-400 mb-8 text-center max-w-xs">Supported: JPG, PNG, BMP (Max 640px internal scaling)</p>
      
      <input type="file" id="pcb-upload" className="hidden" accept="image/*" onChange={handleFileChange} disabled={loading} />
      
      <label 
        htmlFor="pcb-upload" 
        className={`px-8 py-3 rounded-xl font-bold text-sm tracking-widest uppercase cursor-pointer transition-all shadow-lg shadow-blue-500/20 ${loading ? 'bg-slate-700 text-slate-500' : 'bg-blue-600 text-white hover:bg-blue-500 hover:-translate-y-1'}`}
      >
        {loading ? 'Analyzing Neural Network...' : 'Upload PCB Sample'}
      </label>
    </motion.div>
  );
};

export default UploadBox;
