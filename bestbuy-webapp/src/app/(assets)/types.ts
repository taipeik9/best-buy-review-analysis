export type Session = {
  id: string;
  scraping_started: string;
  scraping_finished: string | null;
  done: boolean;
};

export type Review = {
  id: string;
  rating: number;
  title: string;
  content: string;
  date: string;
  reviewer_name: string;
  reviewer_location: string;
  verified_purchase: boolean;
  product_id: number;
  session_id: string;
};

export type Product = {
  id: number;
  title: string;
  short_description: string;
  avg_rating: number;
  rating_count: number;
  regular_price: number;
  sale_price: number;
  category_name: string;
  session_id: string;
};

export type Column = { name: string; id: string };
