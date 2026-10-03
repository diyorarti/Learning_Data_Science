"""
The Laws of probability are fundamental principles that govern the behavior and relationships between events in probability theory.
Hierarchical structure:
├── 1. Event operations
│   ├── Intersection: A ∩ B
│   ├── Union: A U B
│   └── Complement: Aᶜ
│
├── 2. Event relationships 
│   ├── Mutually exclusive
│   ├── Independent
│   └── Dependent
│
└── 3. Probability calculation rules
    ├── Complement rule
    ├── Addition rule
    │   ├── General addition rule
    │   └── Mutually exclusive special case
    ├── Multiplication rule 
    │   ├── General/dependent rule
    │   └── Independent special case
    ├── Conditional probability
    └── Bayes' theorem
""" 
  
# Event Operations
"""
Event Operations are ways of combining or midifying events to create a new event
In probability, an event is a set of outcomes from the sample space. 
        For example:
            Rolling one fair six-sided die.
            Sample Space = {1, 2, 3, 4, 5, 6}

            A event = Rolling an even number
                A = {2, 4, 6}
            B event = Rolling a number greater than 3
                B = {4, 5, 6}
            Now, We can apply event operations to A and B events:
                1. Intersection
                2. Union 
                3. Complement
    Example use cases event operations:
        Customer analysis:
            A = customer purchased
            B = Customer is a returning customer
            A ∩ B = customers purchased and returned 
            this helps measure customer royalty
        Market analysis
            A = Customer saw an advertisement
            B = Customer purchased
            A ∩ B customers saw ads and purchased
            this helps evaluate marketing performance
        Churn Analysis 
            A = customer has a monthly constract
            B = customer churned
            A ∩ B customers have monthly contracts and churned
            this helps indetify high-risk customer groups
        Fraud detection:
            A = transaction amount is unsually high
            B = transaction occured in a new country
            A ∩ B means both suspicious conditions occurred
            A U B means at least one suspicious condition occurred.
        Medical Data:
            A = patient has high blood pressure
            B = patient has diabetes
    

    Intersection:
        Intersection containes outcomes that belong to both events. Symbol:  A ∩ B. Read: A and B
        We have events:
                        A = {2, 4, 6}
                        B = {4, 5, 6}
        Intersection outcomes A ∩ B = {4, 6}
        Rolling a number that is even and greater than 3, only {4, 6} satisfy both conditions
    
    Union:
        The Union contains outcomes that belong to A, B or both. Symbol: A U B. Read: A or B
        We have events:
                        A = {2, 4, 6}
                        B = {4, 5, 6}
        Union outcomes A U B = {2, 4, 5, 6}
        Rolling a number that is even, greater than 3 or satisfies both conditions
    
    Complement:
        Complement contains all outcomes in the sample space that don't belong to the event. Symbol  Aᶜ / A' . Read Not A
        We have event:
                      A = {2, 4, 6}
        Complement of A event outcomes Aᶜ = {1, 3, 5}
        Rolling a number that is not even number         
"""

# Event Relationships
"""
Event relationships describe how two events are connected to each other.
They answer questions such as:
    1. Can the two events happen at the same time ?
    2. Does one event change the probability of the other ?
    3. Are the events unrelated ?

    Mutually exclusive events
        Two events are mutually exclusive when then cannot happen at the same time. 
        Mathematically: A ∩ B = ∅ ---> P(A ∩ B) = 0
        example:
            Rolling one die:
                A event = rolling a 2 
                B event = rolling a 5 
            in one roll, it can't be got both 2 and 5
            So, A event and B event are mutually exlusive
            Their sets: A = {2}, B = {5}
            They have no common outcomes: A ∩ B = ∅

    Independent Event
        Two events are independent when one event doesn't change the probability of the other
        Mathematically: P(B | A) = P(B)
        This means Event A happens , but the probability of event B stays exactly the same.
        example:
            Tossing a coin twice.
            A = heads on the first toss
            B = heads on the second toss
            The first toss doesn't affect the second toss.
            Before first toss --> P(B) = 0.5
            after first toss --> P(B | A) = 0.5 

    Dependent events
        Two events are dependent when one event changes the probability of the other.
        Mathermatically: P(B | A) ≠ P(B) 
        Example: 
            Selecting cards without replacement
            Supposse a big contains: 3 red balls and 2 blue balls
                A event = the first ball is red
                B event = the second ball is red
            Before selecting anything:
                P(B) = 3 / 5
            But suppose the first ball is red and we don't replace it
            Only 2 red balls and 2 blue balls remain:
                P(B | A) = 2 / 4  --> 3/5 ≠ 2 / 4
"""

# Probability calculation rules
"""
Probability calculation rules are common formulas used to calculate the probability of combined or related events

Complement rule:
    Complement rule calculates the probability that event A doesn't happent. P(Aᶜ) = 1 - P(A)
    Example:   P(passing) = 0.8
               P(not passing) = 1 - 0.8 = 0.2

Addition rule:
    Addition rule calculates the probability that Event A or B happens

    General Addition rule:
        General Addition rule is used whens event may overlap, meaning they may happen together: 
        Formula: P(A U B)= P(A) + P(B) - P(A ∩ B)
        Example: Rolling a die
            Sample space S = {1, 2, 3, 4, 5, 6}
                Event A rolling an even number A={2, 4, 6}
                Event B rolling an number greater than 3 B={4, 5, 6}
            Intersection:
                A ∩ B = {4, 6}
            Find the union directly:
                A U B = {2, 4, 5, 6}
                P(A U B) = 4 / 6 = 0.66
            By Formula:
                P(A U B) = P(A) + P(B) - P(A ∩ B) = 3/6 + 3/6 - 2/6 = 0.5 + 0.5 - 0.34 = 0.66

    Mutually exclusive special case 
        Events are mutually exclusive when they can't happen together. A ∩ B = ∅ --> P(A ∩ B) = 0
        Because there is no overlap, there is nothing to substract.
        So Addition rule simplifies to: P(A U B) = P(A) + P(B)
        Example: Rolling a die
            Event A rolling 2:  A = {2}
            Event B rolling 5:  B = {5}
        on one die roll, it can't be roll both  2 and 5, Therefore the events are mutually exclusive. A ∩ B = ∅
        THe probabilities:
            P(A U B) = P(A) + P(B) = P(1 / 6) + P(1 / 6) = 0.16 + 0.16 = 0.32

Multiplication Rule
    Multiplication rule calculates the probability that two events both happen. A ∩ B
    it answers What is the probability that event A happens and B also happens ?

    General/Dependent multiplication rule:
        The general rule is  P(A ∩ B) = P(A) * P(B | A).
        It can also be written in the reverse order: P(A ∩ B) = P(B) * P(A | B)
        Here:
            P(A) -> probability that A happens
            P(B | A) -> probability that B happens after we know A happened
            P(A ∩ B) -> probability that both happen
            Probability of the first event * probability of the second event after the first
        Example:
            Rolling a six sided fair die:
                A event -> Even number -> S={2, 4, 6}
                B event -> a numb > 3  -> S={4, 5, 6}
                these events are dependet
                A ∩ B -> S={4, 6}
            P(A ∩ B) = ?
            P(A) = 3 / 6 = 0.5
            P(B | A) = P(A ∩ B) / P(A) = (2/6) / (3/6) = 0.33 / 0.5 = 0.66
            P(A ∩ B ) = P(A) * P(B | A) = 0.5 * 0.66 = 0.33
            
    Independent-events special case 
        Events are independent when one event doesn't change the probability of the other
        THe rule formula: P(A ∩ B) = P(A) * P(B)
        Example: Tossing a coin twice
            A event = Heads on the first toss
            B event = Heads on the second toss
        For a fair coin:
            P(A) = 1 / 2
            P(B) = 1 / 2
        So: P(A ∩ B) = 1/2 * 1/2 = 1/4 = 0.25
        So P(two heads) = 0.25 = 25%
        THe sample space:
            S={HH,HT,TH,TT} 
            P(HH) = 25%

Conditional Probability
    Conditional Probability is the probability of an event after we receive additional information that another event has already happened.
    It answers: What is the probability of event A, given that event B has happened.
    The notation is P(A | B) , read it as "THe probability of A, given B" 
    THe main idea: the sample space becomes smaller. 
    Ordinary probability considers the complete sample space: S
    Conditional probability considers only the outcomes that satisfy the given condition.
    So when we know B happened : The sample space is reduced from S to B 
    Example:
        Rolling a fair six-sided die.
        THe complete sample sapce: S = {1, 2, 3, 4, 5, 6}
        Event A: rolling an even number A={2, 4, 6}
        EVent B: rolling a num greater than 3 B={4, 5, 6}
        Now Calculate: P(A | B)
        What is the probability of en even number(A event), given that we already know the result is greater than 3. 
        Calculation:
            1-step: We use B as the sample space because we know result is greate than 3.
                new sample space B = {4, 5, 6}, no longer consider {1, 2, 3}
            2-step: Find outcomes that satisfy A event(even number).
                sample space B={4, 5, 6} --> even numbers = {4, 6}
                A ∩ B = {4,6}
            3-step: Compare with the new sample space. 
                3 outcomes in B = {4, 5, 6}, it is both sample space and event B 
                2 outcomes belong to A(event) = {4, 6}
                SO: P(A | B) = 2 / 3 = 0.667 = 66.7% 
    
    Conditional Probability Formula: P(A | B) = P(A ∩ B) / P(B). It can be used only when P(B) > 0 
        P(A | B) -> A is the target event, B is the condition
        P(A ∩ B) -> Intersection operation
        P(B) -> probability of condition
        Since we already know that B event happened, B event outputs become new sample space
    
    Direction of the Condition
        It tells us: which event is the target whose probability we want
                     Which event is the given condition that becomes the new reference group
        P(A | B)  Target is A event, B is the condition 
        P(B | A)  Target is B event, A is the condition

Bayes' Theorem 
    Bayes' Theorem is a formula used to reverse the direction of the conditional probability
    Suppose: we know P(B | A), but we need P(A | B)
    Bayes' Theorem helps us to calculate it.  
    Formula: P(A | B) = P(B | A) * P(A) / P(B)
    Here:
        A = the event we are interested in
        B = The happened event / the observed evidence
        P(A) = Probability of A before observing B
        P(B | A) = probability of B when given A 
        P(B) = overall probability of observing B
        P(A | B) = updated probability of A after observing B 
    Main idea of Bayes' Theorem --> Revering the direction
        P(A | B) -> Probability of B, given A
        P(B | A) -> Probability of A, given B
        P(A | B) ≠ P(B | A)

    Example: University has 100 students
        40 study Data science
        60 study Python
        30 study both Data science and Python 
            A event = student studies Data science
            B event = student studies Python 
            We want P(A | B) 
            this means among students who study Python, what is the probability that a student study Data Science ? 
        Implementation: 
            1-step: P(B | A) among 40 data science studnets, 30 study Python. P(B | A) = 30 / 40 = 0.75
                    This means 75% of data science studnets study python. 
            2-step P(A) There are 40 data science students among 100 students: P(A) = 40 / 100 = 0.40
            3-step P(B) THere are 60 python students among 100 students P(B) = 60 / 100 = 0.60 
            4-step Apply Bayes' Theorem P(A | B) = P(B | A) * P(A) / P(B) = 0.75 * 0.40 / 0.60 = 0.50
        So:
            75% Data science students study Python 
            50% Python students study Data science
"""  

