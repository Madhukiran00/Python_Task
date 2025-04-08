para='''Engineering is the creative application of scientific 
principles and mathematical methods to design, develop, and 
improve structures, machines, systems, and processes, aiming 
to solve problems and enhance efficiency. Engineers use their 
knowledge to invent, build, and maintain infrastructure, 
technology, and other essential aspects of modern life, focusing
on practical solutions and innovation. This field encompasses 
diverse specialties, from civil and mechanical to electrical and
chemical engineering, each tackling specific challenges and 
contributing to societal progress. Engineering is a problem-solving 
discipline that requires creativity, analytical skills, and a deep 
understanding of scientific and technical principles. Ultimately,
engineering plays a crucial role in shaping our world and improving
the quality of life for everyone. '''

li=para.split(" ")
if len(li)>60:
    print("Valid Paragraph")
else:
    print("Not a Valid Paragraph")
     