## Linux CLI syntax

$ yn powershell tutorial 2

    https://www.youtube.com/watch?v=IHrGresKu2w
    https://www.youtube.com/watch?v=sQm4zRvvX58

<br>

## Python module use

    import yn
    
We use a trailing result count count in-line:
    
    yn.main("powershell tutorial 2")
    
    ['https://www.youtube.com/watch?v=IHrGresKu2w',
     'https://www.youtube.com/watch?v=sQm4zRvvX58']
     
or use a separate `count` parameter:

    yn.main "powershell tutorial", count=2)
    
    ['https://www.youtube.com/watch?v=IHrGresKu2w',
     'https://www.youtube.com/watch?v=sQm4zRvvX58']
