
import React from 'react';

const Expertise: React.FC = () => {
  const services = [
    { title: 'Brand Identity', description: 'Crafting unique visual languages that communicate core values and resonate with audiences.' },
    { title: 'Digital Strategy', description: 'Developing comprehensive roadmaps for growth in a rapidly evolving technological landscape.' },
    { title: 'Creative Direction', description: 'Leading artistic vision and execution across multidisciplinary platforms and media.' },
    { title: 'Interactive Design', description: 'Building engaging, human-centric experiences that bridge the gap between user and brand.' }
  ];

  return (
    <section id="expertise" className="py-32 px-6 bg-[#1c1c1c] text-white overflow-hidden">
      <div className="max-w-7xl mx-auto">
        <div className="grid lg:grid-cols-2 gap-24 items-start">
          <div className="sticky top-32">
            <h2 className="text-xs uppercase tracking-[0.3em] font-bold text-emerald-500 mb-8">Expertise</h2>
            <h3 className="text-5xl md:text-7xl font-serif leading-tight">
              Design as a <br />
              <span className="italic opacity-60">System of</span> <br />
              Growth.
            </h3>
            <p className="mt-12 text-xl text-neutral-400 font-light max-w-md leading-relaxed">
              We don't just build assets; we engineer ecosystems where brands can thrive and evolve organically.
            </p>
          </div>
          
          <div className="space-y-16">
            {services.map((service, idx) => (
              <div key={idx} className="group border-b border-neutral-800 pb-12 last:border-0">
                <span className="text-xs font-mono text-neutral-600 mb-4 block">0{idx + 1}</span>
                <h4 className="text-3xl font-medium mb-6 group-hover:text-emerald-400 transition-colors">{service.title}</h4>
                <p className="text-neutral-400 text-lg leading-relaxed max-w-xl">
                  {service.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Expertise;
