export interface Analyse {
  _id: {
    code_cip: string;
    year?: string;
    month?: string;
    day?: string;
  };
  count: number;
}
