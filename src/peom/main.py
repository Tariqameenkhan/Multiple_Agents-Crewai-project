from crewai.flow import Flow, start, listen
from peom.crews.poem_crew.poem_crew import DevCrew

class DevFlow(Flow):

    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "problem":"write python code for addtion two numbers"
            }
        )
        return output.raw
    


def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)