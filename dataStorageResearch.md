# Research on Data Storage in Python

## Summary

The scope of this project has a simple use-case, essentially storing a persistant simple list with a very trivial relationship (a song has one or more links/files connected to it).

Serialization or "store by file" is useful for data transmission, brief development time, and storing unstrucutured/binary data.

Databases are good for scalable complex data storage. There is increased development overhead, but for a simple usecase there are lightweight solutions on offer suchas SQLite.

It is suggested that the project moves forward by using SQLite for data storage. Serialization can be used later on to enable sharing of data, suchas migrating data to a different machine or to a friend.

## Use Case

This tool is designed to provide easy storage and access of links and local files for people learning music. The idea is that they are trying to learn a song, so they find a tab on a webpage or a pdf to store locally. They can then use this tool to store the links and files related to their learning of the song. There may be multiple files related to a single song. They can then access their links and files by using the "learn" flag which will open the files in their browser.

There are many ways to skin this cat, and this is the way I wanted to do it. I'm going to explore the various data storage methods in Python and use that as a starting point to learn more about data storage in general.

## Technologies and Tools

### Serialization

Serialization encompasses multiple tools and formats. There are simple text methods: CSV, XML, JSON, YAML. They are human readable and have low performance due to the string parsing required to operate. These are better suited to data transmission rather than storage. There are Binary methods (non human readable) for python such as NumPy Array (flat) and Pickle (nested). Keep in mind that although some methods are best for transmission, if the data set is trivial (like this project) they may yield better performance.

Lastly Google created Protocol Buffers (Protobufs) to work across different platforms and languages with good performance.

#### Strengths - Serialization

- Local storage
- Fast development time
- Unstrucured or raw data from your program.

#### Weaknesses - Serialization

- Complex/large data sets

### Databases

Tried and true storage medium. Good for large amounts of complex data with many realationships.

#### Strengths - Databases

- Large data sets, performance gains due to indexing
- Multiple users/instances, transactional nature of operation
- Centralized storage, many users to one large location
- Searching and analysis of data

#### Weaknesses - Databases

- Can be difficult for the user to handle, not as intuitive, must provide interface
- Does not "transfer" well between applications without extra dev work

## Options for Project

Pickle is an easy python exclusive serialization tool, would be interesting to use for the sake of learning. If learning about serialization is important, learning Google's ProtoBufs is like a better learning medium and would be more useful IRL.

SQLite is a good DB solution that is used heavily within the embedded dev space. NoSQL is better for "big data" purposes, less applicable for this app.

I suggest using SQLite to start and get things working. Try using Protobufs later on so people can backup their data or send them to their other devices.

## Sources

https://docs.python-guide.org/scenarios/serialization/
https://stackoverflow.com/questions/765090/serializing-vs-database
https://stackoverflow.com/questions/201568/when-would-i-use-xml-instead-of-sql/201594#201594
https://softwareengineering.stackexchange.com/questions/190482/why-use-a-database-instead-of-just-saving-your-data-to-disk
