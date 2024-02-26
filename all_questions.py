# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative consider pairwise distances between points which makes it less sensitive to outliers than k-means."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "For k-means, where the centroids start can lead to differet outcomes but since agglomerative hierarchical clustering are deterministic algorithms which result in the same clustering for every run."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "k-means can be efficient in certain situations but we can't make the blanket statement that it is the most efficient clustering algorithm."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "For k-means each centroid is adjusted based on the mean of the points assigned to it and the points are reassigned to the nearest centroid."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "When SSE decreases this indicates that the points within the clusters are getting closer to tge centroids which leads to an increased cohesion within the clusters."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An increase in SSb implies that the clusters are further apart from each other, leading to greater separation between clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    # Add a different explanation
    answers["(g) explain"] = "Cohesion and separation are independent in k-means clustering because cohesion focuses on minimizing te within-cluster variation while separation focuses on maximiazing the between-cluster variation."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    # Add a different explaination
    answers["(h) explain"] = "Both this values can change as the centroids and cluster assignments are updated during each iteration of the clustering algorithm."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    # Add a different explanation
    answers["(i) explain"] = "Cohesion and separation are independent metrics so increasing one does not guarantee an increase in the other."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (a**2 + b**2 + c**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*(R**2 + (R/2)**2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set({'Group B', 'Group A'})

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: set
    answers["(b)"] = set({'Group C', 'Group A'})

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set({'I', 'J', 'E', 'F', 'C', 'L', 'M', 'B'})

    # type: set
    answers["(a) boundary"] = set({'G', 'D'})

    # type: set
    answers["(a) noise"] = set({'A', 'H'})

    # type: set
    answers["(b) cluster 1"] = set({'E', 'F', 'C', 'B', 'G', 'D'})

    # type: set
    answers["(b) cluster 2"] = set({'M', 'I', 'J', 'L'})

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set({'I', 'J', 'E', 'F', 'C', 'L', 'M', 'G', 'D', 'B'})

    # type: set
    answers["(c)-a boundary"] = set({'A', 'H'})

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set({'H', 'I', 'J', 'E', 'F', 'C', 'L', 'M', 'G', 'D', 'A', 'B'})

    # type: set
    answers["(c)-b cluster 2"] = set('A')

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""
    
    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["Hierarchical", "overlapping", "partial"]

    # type: list
    answers["(b)"] = ["Partitional", "exclusive", "complete"]

    # type: list
    answers["(c)"] = ["Partitional", "fuzzy", "complete"]

    # type: list
    answers["(d)"] = ["Hierarchical", "overlapping", "partial"]

    # type: list
    answers["(e)"] = ["Partitional", "Exclusive", "partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "partial because some student may not receive a grade in the class if they get an I for Incomplete."
    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
