export interface Consultation {
  id: number
  patientName: string
  notes: string
  diagnosisCodes: string[]
}

export interface Diagnosis {
  code: string
  description: string
}