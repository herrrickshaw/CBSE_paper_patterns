"""Per-question marks + attempt rules, taken from each paper's General Instructions.
Each entry: (q_from, q_to, marks_per_question, answer_any_or_None, block_label)
answer_any=None means every question in the range is compulsory.
"""
ACADEMIC = {
 "History":      [(1,21,1,None,"A: MCQ"),(22,27,3,None,"B: Short answer 60-80w"),
                  (28,30,8,None,"C: Long answer 300-350w"),(31,33,4,None,"D: Source-based"),
                  (34,34,5,None,"E: Map")],
 "Political Science":[(1,12,1,None,"A: MCQ"),(13,18,2,None,"B: Short answer 50-60w"),
                  (19,23,4,None,"C: Long answer-I 100-120w"),(24,26,4,None,"D: Passage/Cartoon/Map"),
                  (27,30,6,None,"E: Long answer-II 170-180w")],
 "Economics":    [(1,10,1,None,"A Macro: MCQ"),(11,12,3,None,"A Macro: SA-I 60-80w"),
                  (13,15,4,None,"A Macro: SA-II 80-100w"),(16,17,6,None,"A Macro: LA 100-150w"),
                  (18,27,1,None,"B Indian Econ Dev: MCQ"),(28,29,3,None,"B: SA-I 60-80w"),
                  (30,32,4,None,"B: SA-II 80-100w"),(33,34,6,None,"B: LA 100-150w")],
 "Accountancy":  [(1,16,1,None,"Part A: MCQ"),(17,20,3,None,"Part A: Short answer"),
                  (21,22,4,None,"Part A: Long answer-I"),(23,26,6,None,"Part A: Long answer-II"),
                  (27,30,1,None,"Part B: MCQ"),(31,32,3,None,"Part B: Short answer"),
                  (33,33,4,None,"Part B: Long answer-I"),(34,34,6,None,"Part B: Long answer-II")],
 "Computer Science":[(1,21,1,None,"A"),(22,28,2,None,"B"),(29,31,3,None,"C"),
                  (32,35,4,None,"D"),(36,37,5,None,"E")],
}
SKILL = {  # bundles in Sec A carry group marks; Sec B blocks have answer_any
 "Artificial Intelligence":[(1,1,4,None,"A: Employability (any 4 of 6 x1)"),(2,5,5,None,"A: Subject (any 5 of 6 x1)"),
                  (6,10,2,3,"B: Employability 20-30w"),(11,16,2,4,"B: Subject 20-30w"),(17,21,4,3,"B: Subject 50-80w")],
 "Information Technology":[(1,1,4,None,"A: Employability"),(2,2,5,None,"A"),(3,3,6,None,"A"),(4,6,5,None,"A"),
                  (7,11,2,3,"B: Employability 20-30w"),(12,16,2,3,"B: Subject 20-30w"),
                  (17,19,3,2,"B: Subject 30-50w"),(20,24,4,3,"B: Subject 50-80w")],
 "Typography and Computer Applications":[(1,1,4,None,"A: Employability"),(2,2,5,None,"A"),(3,3,6,None,"A"),(4,6,5,None,"A"),
                  (7,11,2,3,"B: Employability 20-30w"),(12,16,2,3,"B: Subject 20-30w"),
                  (17,19,3,2,"B: Subject 30-50w"),(20,24,4,3,"B: Subject 50-80w")],
 "Financial Markets Management":[(1,1,4,None,"A: Employability"),(2,2,5,None,"A"),(3,3,6,None,"A"),(4,6,5,None,"A"),
                  (7,11,2,3,"B: Employability 20-30w"),(12,16,2,3,"B: Subject 20-30w"),
                  (17,19,3,2,"B: Subject 30-50w"),(20,24,4,3,"B: Subject 50-80w")],
 "Taxation":     [(1,1,4,None,"A: Employability"),(2,2,5,None,"A"),(3,3,6,None,"A"),(4,6,5,None,"A"),
                  (7,11,2,3,"B: Employability 20-30w"),(12,16,2,3,"B: Subject 20-30w"),
                  (17,19,3,2,"B: Subject 30-50w"),(20,24,4,3,"B: Subject 50-80w")],
 "Web Applications":[(1,1,4,None,"A: Employability"),(2,2,5,None,"A"),(3,3,6,None,"A"),(4,6,5,None,"A"),
                  (7,11,2,3,"B: Employability 20-50w"),(12,17,2,3,"B: Subject 20-50w"),
                  (18,20,3,2,"B: Subject 30-90w"),(21,25,4,3,"B: Subject 30-100w")],
 "Engineering Graphics":[(1,14,1,None,"A: MCQ"),(15,18,1,None,"B: Case paragraph 1"),(19,22,1,None,"B: Case paragraph 2"),
                  (23,23,27,None,"B: Assembly drawing"),(24,24,13,None,"C: Isometric"),(25,25,8,None,"C: Thread/Nut")],
}
