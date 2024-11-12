from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Sheldon Lee Cooper,[4][5] Ph.D., Sc.D.,[6] is a fictional character and one of the main protagonists in the CBS television series The Big Bang Theory and its spinoff series Young Sheldon, portrayed by actors Jim Parsons and Iain Armitage respectively (with Parsons as the latter series' narrator).[7] For his portrayal, Parsons won four Primetime Emmy Awards, a Golden Globe Award, a TCA Award, and two Critics' Choice Television Awards. The character's childhood is the focus of Young Sheldon, in which he grows up in East Texas with his family Missy Cooper, George Cooper Sr., George Cooper Jr., Mary Cooper and his grandmother, Connie Tucker, as a child prodigy.

The adult Sheldon is a senior theoretical physicist at the California Institute of Technology (Caltech), and for the first ten seasons of The Big Bang Theory shares an apartment with his colleague and best friend, Leonard Hofstadter (Johnny Galecki); they are also friends and coworkers with Howard Wolowitz (Simon Helberg) and Rajesh Koothrappali (Kunal Nayyar). In season 10, Sheldon moves across the hall with his girlfriend Amy Farrah Fowler (Mayim Bialik), in the former apartment of Leonard's wife Penny (Kaley Cuoco).[8]

He has a genius-level IQ of 187. In The Big Bang Theory, it is said that his and Leonard's IQs add up to 360, meaning Leonard has an IQ of 173. In Young Sheldon Season 7 Episode 7, when Sheldon was studying at home and was commanded to answer the phone, he became annoyed and stated that he is treated like a receptionist at home, despite having an IQ of 187, directly confirming the number. However, he displays a fundamental lack of social skills, a tenuous understanding of humor (always ending with "bazinga"), and difficulty recognizing irony and sarcasm in other people, although he himself often employs them. He exhibits highly idiosyncratic behavior and a general lack of humility, empathy, and toleration. These characteristics provide the majority of the humor involving him, which are credited with making him the show's breakout character.[9][10][11][12] Some viewers have asserted that Sheldon's personality is consistent with autism spectrum disorder (or what used to be classified as Asperger's Syndrome).[11][13] Co-creator Bill Prady has stated that Sheldon's character was neither conceived nor developed with regard to Asperger's,[13] although Parsons has said that in his opinion, Sheldon "couldn't display more facets" of Asperger's syndrome.[14]
"""

if __name__ == "__main__":
    print("Hello Lang AI!")

    summary_template = """
        Given the information {information} about a person, I want you to create :
        1. A short summary of the life story.
        2. Identify what this person is doing today.
        3. One fun fact about this person 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    result = chain.invoke(input={"information": information})

    print(result)
