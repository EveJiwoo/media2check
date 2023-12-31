# Filter fake news out by Media2Check #

Fake news articles that are intentionally false designed to manipulate have been used to influence politics and promote advertising. Stories that are untrue and that intentionally mislead readers have caused growing mistrust among American people. In a few cases, this mistrust results in incivility, protest over imaginary events, or violence. People, organizations, and governments use fake news for a couple of different reasons. They intensify social conflict to undermine people’s faith in the democratic process and people’s ability to work together. 

<p align="center">
  <img src="https://github.com/media2check/media2check/assets/145739444/f30197a2-f81c-4bbe-a732-8f2868c268cc" width="18%">
  <img src="https://github.com/media2check/media2check/assets/145739444/563b8f90-8f07-43a6-a4f6-f6c3cb9c1072" width="18%">
  <img src="https://github.com/media2check/media2check/assets/145739444/49b91605-60bc-4555-add7-b1888ffcae72" width="18%">
  <img src="https://github.com/media2check/media2check/assets/145739444/80a2a74c-e096-44e9-8ddc-eb44c24a228f" width="18%">
  <img src="https://github.com/media2check/media2check/assets/145739444/c4cfa4d6-ae53-4f1d-aaf0-bdc7d6a77ff8" width="18%">
</p>
  
The New York Times wrote an article to expose these fake news posts shared on an SNS platform. Other text based SNS platforms showed a similar trend of sharing false information.

## Team work ##
Our team was formed by friends who are interested in the media industry and technology. It all started when some of our team members felt like victims from knowing that the articles they’ve read from well known social media apps were fake news, but they scoured the internet to see if there was an easy solution to stop falling into this manipulation. 

We used [draw.io](https://www.draw.io/) to collaborate on program architecture. Each member thought of ways to filter fake news using the information available to the public. Then we thought of a case when SNS platforms provide access to private information. 

<p align="center">
  <img src="https://github.com/media2check/media2check/assets/145739444/f63e1051-d071-404e-8485-9a34fd893f08" width="70%">
</p>

Reviewing all posts uploaded on SNS platforms is intensive work so we chose to review posts that are trending. Facebook does not provide API to the public so we worked on twitter. 

## Methods to filter ##

Goal was to filter fake news before spreading too much so we had to make a model which can make decisions fast. To achieve this, we focused on:

- Source check
- Author evaluation
- Cross-reference
- Spread pattern

Source check was done by comparing well-established news outlets. Using many sources including Ad Fontes Media, we could list up media companies to check the source of SNS posts. 

<p align="center">
  <img src="https://github.com/media2check/media2check/assets/145739444/7ee7d955-2659-4fbc-9fc6-18edc727ddd4" >
</p>

Coding to check for text similarity, we used Python library spaCy because it is open source. There are better API options with higher accuracy and more functionalities but we chose not to use because there is cost per processing. 
SNS post texts are compared to many articles produced by news outlets. Just like plagiarism detection, our goal is to find how similar the text is with articles from news outlets. Score for text similarity ranges from [0, 1]. If the score is above a certain threshold, we can say that this post is similar to a reliable news source and it is okay to pass. 



It is important to find the original uploader of posts and determine credentials and expertise in the subject matter. Anonymous or pseudonymous sources are given low scores to check further. X (formerly Twitter) provides such an API to determine the original uploader of a post. Using this information, original accounts can be found and apply the scoring model for reliability as well.

Fake news spread patterns are different from natural ones. From the paper by Zhao, Z., Zhao, J., Sano, Y. et al. ["Fake news propagates differently from real news even at early stages of spreading"](https://rdcu.be/dnJuY) EPJ Data Sci. 9, 7 (2020), it shows the difference in nodes. 

<p align="center">
  <img src="https://github.com/media2check/media2check/assets/145739444/5c4e2faa-f969-4eaa-9ad6-35f3bf5c315d" width = "60%" >
  
</p>

 Examples of fake and real news diagram from the above paper mentioned. 
 
 (B) Fake news example
 (C) Real news example
 (D) Fake news example
 (E) Real news example

Using these four methods, our team was able to create a meaningful project which can help identify fake news and act early to prevent the spread. 


