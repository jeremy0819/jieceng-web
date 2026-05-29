
import React, { useState } from 'react';

const OptimizedImage: React.FC<{src: string, alt: string, className?: string}> = ({ src, alt, className }) => {
  const [isLoaded, setIsLoaded] = useState(false);
  return (
    <div className={`relative overflow-hidden bg-neutral-100 ${className}`}>
      {!isLoaded && <div className="absolute inset-0 bg-neutral-100 animate-pulse"></div>}
      <img src={src} alt={alt} loading="lazy" onLoad={() => setIsLoaded(true)} className={`w-full h-full object-cover transition-opacity duration-1000 ${isLoaded ? 'opacity-100' : 'opacity-0'}`} />
    </div>
  );
};

export default OptimizedImage;
