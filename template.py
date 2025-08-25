# prompt_templates.py
category_PROMPTS = {
    # 推理 (Reasoning) - 0
    0: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on aggregating multiple items, types, options, or counts.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on aggregation, listing, or counting.\n\n###Example\nToyota Camry , how many hybrid variations of this car were there in 2024 ?     the number of variants of the Toyota Camry hybrid in 2024 is 4 or 5.",

    # 比较 (Comparison) - 1
    1: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on comparing attributes such as size, quantity, price, performance, or features between two items.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on comparison of two items.\n\n###Example\nnorthern cardinal , which looks more red, the male or female of this species?    the male northern cardinal and the female northern cardinal, looks more red.",
  
    # 聚合 (Aggregation) - 2
    2: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on aggregating multiple items, types, options, or counts.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on aggregation of multiple items, types, or quantities.\n\n###Example\npaint brushes, what are the different parts of these?    the parts of paint brushes are the bristles, ferrule, and handle.",

    # 简单识别 (Simple Recognition) - 3
    3: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on identifying the visible entity, including its name, kind, brand, or textual content.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on identifying the visible entity, text, or object.\n\n###Example\nsign says winterfest , what does the name on the sign say?   the name on the sign is winterfest.",

    # 简单知识 (Simple Knowledge) - 4
    4: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on retrieving factual knowledge, definitions, classifications, or explanations related to the visible entity.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on retrieving factual knowledge or explanation.\n\n###Example\nthe tradition of the nativity scene, from which country does the tradition of this come from?  the tradition of the nativity scene comes from Italy.",

    # 多跳 (Multi-hop) - 5
    5: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on multi-step reasoning that may require chaining information from external sources or prior knowledge.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on multi-hop reasoning or chained information retrieval.\n\n###Example1\nQuestion: is the author this book still alive?  \nImage: In the image the book's author is Ruth Rendell.\nOutput: the book's author in the image is Ruth Rendell, is the author this book still alive? Ruth Rendell, author of Dark Corners, passed away in 2015."
}
category_PROMPTS_self = {
    # 推理 (Reasoning) - 0
    0: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on aggregating multiple items, types, options, or counts.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on aggregation, listing, or counting.\n\n###Example\nToyota Camry , how many hybrid variations of this car were there in 2024 ?     the number of variants of the Toyota Camry hybrid in 2024 is 4 or 5.",

    # 比较 (Comparison) - 1
    1: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on comparing attributes such as size, quantity, price, performance, or features between two items.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on comparison of two items.\n\n###Example\nnorthern cardinal , which looks more red, the male or female of this species?    the male northern cardinal and the female northern cardinal, looks more red.",

    # 聚合 (Aggregation) - 2
    2: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on aggregating multiple items, types, options, or counts.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on aggregation of multiple items, types, or quantities.\n\n###Example\npaint brushes, what are the different parts of these?    the parts of paint brushes are the bristles, ferrule, and handle.",

    # 简单识别 (Simple Recognition) - 3
   3: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.  \n\nBased on the visible content in the image, directly identify and describe the key entity's name, kind, brand, or textual content.  \n\nQuestion: {query}\n\n###Output\nProvide a direct answer based on image content (less than 30 words)!   If the entity is visible:\n- Identify its exact name, kind, or brand\n- Recognize any visible text\n- If you think this question can be answered only based on the image or internal knowledge, then directly answer the question about the entity in the picture.\nDescribe specific attributes\nIf you cannot identify the entity based on the image, respond with 'I don't know'.  \n\n###Example\nsign says winterfest , what does the name on the sign say?     the name on the sign is winterfest.  \n\nbook cover showing 'The Great Gatsby' , who is the author of this book?     the author of The Great Gatsby is F. Scott Fitzgerald.",

    # 简单知识 (Simple Knowledge) - 4
    4: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on retrieving factual knowledge, definitions, classifications, or explanations related to the visible entity.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on retrieving factual knowledge or explanation.\n\n###Example\nthe tradition of the nativity scene, from which country does the tradition of this come from?  the tradition of the nativity scene comes from Italy.",

    # 多跳 (Multi-hop) - 5
    5: "Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping, Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.\n\nPlease generate search relevant sentences based on the questions raised by the entities in the figure. Focus on multi-step reasoning that may require chaining information from external sources or prior knowledge.\n\nEven if the specific entity is not directly mentioned in the question, please output its name, kind, or brand based on image content.\n\nQuestion: {query}\n\n###Output\nSummarize the image with one sentence describing key entity about its names, kinds, or brand (less than 30 words)!\nIf you cannot identify individuals based on the images, just output the question {query}, do NOT output image caption.\nSearch-relevant sentence focusing on multi-hop reasoning or chained information retrieval.\n\n###Example1\nQuestion: is the author this book still alive?  \nImage: In the image the book's author is Ruth Rendell.\nOutput: the book's author in the image is Ruth Rendell, is the author this book still alive? Ruth Rendell, author of Dark Corners, passed away in 2015."
}
DOMAIN_PROMPTS = {
    # Animal-related queries
    12: "Describe the animal in the image including: species,name, physical characteristics, actions, and environment. Focus on distinctive features.",
    
    # Shopping-related queries
    4: "Identify product details including: brand names, product type, price indicators, logos, slogans, product packaging, any marketing messages visible,and purchase locations visible in the image.",
    
    # Plants and gardening
    5: "Describe plant characteristics including: species, growth stage, health indicators, and gardening tools visible in the image.",
    
    # General object recognition
    3: "List key objects in the image with their attributes: name,type, color, size, material, and spatial relationships.",
    
    # Math and science
    2: "Identify scientific or mathematical elements including: symbols, equations, diagrams, technical notations, experimental data, or graphs visible in the image. Focus on contextual relevance and functional details.if you can work it out, give the description and the answer",
    
    # Vehicles
    9: "Describe vehicle details including: make/model, vehicle type, color, visible damage and other information.",
    
    # Default template
    7: "Summarize the image with one sentence describing key elements.",
    
    # Text understanding
    11: "Extract text elements: content transcription, language/formatting, contextual meaning, technical terms, comparative analysis, and historical links, prioritizing accuracy and contextual clarity.",
    
    # Brand-related
    8: "Identify architectural or artistic elements in the image including: style, structure details, materials used, notable features, and any visible historical or cultural context.",
    
    # Local information
    6: "Identify and describe key elements of the food or supermarket product in the image, including:Product Identification :Name, type, and primary ingredients ,Brand & Origin : Brand name, manufacturer, country or region of origin.",
    
    # Book-related
    1: "Describe book details including: title, author, cover design, ISBN, and any visible text excerpts.",
    
    # Default fallback generl object recognition
    10: "Summarize the image with one sentence describing key elements.It might be related to issues in sports, finance or other fields. You still describe key features, names, or proper nouns, etc"
# DOMAIN_PROMPTS = {
    # Animal-related queries
    # 0: "Describe the animal in the image including: species, physical characteristics, actions, and environment. Focus on distinctive features.",
    
    # # Shopping-related queries
    # 1: "Identify product details including: brand names, product type, price indicators, and purchase locations visible in the image.",
    
    # # Plants and gardening
    # 2: "Describe plant characteristics including: species, growth stage, health indicators, and gardening tools visible in the image.",
    
    # # General object recognition
    # 3: "List key objects in the image with their attributes: type, color, size, material, and spatial relationships.",
    
    # # Math and science
    # 5: "Identify scientific elements including: symbols, equations, diagrams, or any technical notations visible in the image.",
    
    # # Vehicles
    # 6: "Describe vehicle details including: make/model, vehicle type, color, visible damage, and license plate information.",
    
    # # Default template
    # 4: "Summarize the image with one sentence describing key elements.",
    
    # # Text understanding
    # 7: "Extract and describe any visible text elements including: language, content, formatting, and text layout.",
    
    # # Brand-related
    # 8: "Identify brand elements including: logos, slogans, product packaging, and any marketing messages visible.",
    
    # # Local information
    # 9: "Identify local landmarks, street signs, store fronts, or geographic features visible in the image.",
    
    # # Book-related
    # 11: "Describe book details including: title, author, cover design, ISBN, and any visible text excerpts.",
    
    # # Default fallback
    # 10: "Summarize the image with one sentence describing key elements."

    # "type": "text", "text": f"Entities may involve multiple fields including 'Book, Food, General object recognition, Math and science, Nature, Pets, Plants and Gardening, Shopping,Sightseeing, Sports and games, Style and fashion, Text understanding, Vehicles, and Others'.  Please generate search relevant sentences  based on the questions raised by the entities in the figure."
    #             "The entities are diverse and may not appear in the question, but this does not affect your output of the entity name ,kinds,brand."
    #             "\n Question：{query}"
    #             "###Output"
    #             "Summarize the image with one sentence describing key entity about it's names,kinds or brand less than 20 words!"
    #             "Question{query} and search relevant sentences also should be output. "
    #             "If you cannot identify individuals based on the images,you can just output the question{query},don't ouput image caption."
    #             "###Example0: Animal-related queries
    #             "the american pit bull terrier ,question： how does the size of this breed compare to the english staffordshire bull terrier?  Height,weight,size comparison between American Pit Bull Terrier and English Staffordshire Bull Terrier"
    #             "###Example1: Shopping-related queries
    #             "a pair of skis leaning against a door, with the brand name \"ROSSIGNOL\" visible on the side of the ski.question： which of these ski brands is older?  Rossignol skis ."
    #             "###Example2: Plants and gardening
    #             "the inchplant , question：in what country is this plant considered invasive?  the inchplant is invasive plant . "
    #             "###Example3: General object recognition
    #             "glove ,question： what did o.j. simpson's lawyer say about this?  o.j. simpson's lawyer say about the gloves in the simpson trial."
    #             "###Example5: Math and science
    #             "a piece of paper with the numbers 49 and 55 on it, with a white outlet in the background.  The numbers on the paper are likely a math problem or equation about multiplication . question：solve this problem.  The image shows a hand holding a piece of paper with a mathematical equation on it, specifically 49 x 55.  "
    #             "###Example6: Vehicles "
    #             " Toyota Camry , question： how many hybrid variations of this car were there in 2024 ?  variants of the toyota camry hybrid in 2024."
    #             "###Example7: Text understanding
    #             " a collage of various video game characters, including Mario, Link, and Kratos.question：how many years ago did this character with the red stripe on their face first appear in a video game?  Kratos with the red stripe on his face first appear in a video game."
    #             "###Example8: Brand-related
    #             "Historic Hotels of America ,question： are there more of these in puerto rico or hawaii? Historic Hotels of America in Puerto Rico and Hawaii."
    #             "###Example9: Local information
    #             "a hand holding a box of Cinnamon Toast Crunch cereal , question：how many slogans have there been for this cereal?  slogans for cinnamon toast crunch."
    #             "###Example10:"
    #             " northern cardinal , question：which looks more red, the male or female of this species?  the male northern cardinal and the female northern cardinal,."
    #             "###Example11: Book-related
    #             " a book titled \"Percy Jackson and the Olympians: The Chalice of the Gods\" by Rick Riordan.  The book is a fantasy novel about Greek mythology.  question：where does this book fit in the percy jackson series?  The book 'Percy Jackson and the Olympians: The Chalice of the Gods'  novel in the Percy Jackson series,"

                                                
}

