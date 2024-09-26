export type Session = {
  id: string;
  scraping_started: string;
  scraping_finished: string;
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