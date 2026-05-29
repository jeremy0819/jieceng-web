
export interface Project {
  id: string;
  title: string;
  category: 'residential' | 'commercial' | 'public';
  categoryLabel: string;
  description: string;
  imageUrl: string;
  year: number;
  details?: string;
  highlights?: string[];
  techSpecs?: { label: string; value: string }[];
  featuredTechnologies: string[];
}

export interface ProjectFilters {
  categories: string[];
  technologies: string[];
}

export interface ChatMessage {
  role: 'user' | 'assistant';
  text: string;
}

export enum Section {
  HERO = 'hero',
  WORK = 'work',
  EXPERTISE = 'expertise',
  EVALUATION = 'evaluation',
  ABOUT = 'about',
  CONTACT = 'contact'
}
