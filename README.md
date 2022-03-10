this small poc was made to be sure how to run sync stuff in async way:

```
example output (split manually by time):

2022-03-09 14:47:07,164 INFO - 1pro msg 1 thread 69088
2022-03-09 14:47:07,166 INFO - 1pro msg 1 thread 32000 instance 10320 waiting
2022-03-09 14:47:07,166 INFO - 2pro msg 1 thread 69088
2022-03-09 14:47:07,166 INFO - 2pro msg 1 thread 39296 instance 10320 waiting
2022-03-09 14:47:07,166 INFO - 3pro msg 1 thread 69088
2022-03-09 14:47:07,166 INFO - 3pro msg 1 thread 46592 instance 10320 waiting

2022-03-09 14:47:10,170 INFO - 1pro msg 2 thread 69088
2022-03-09 14:47:10,171 INFO - 2pro msg 2 thread 69088
2022-03-09 14:47:10,172 INFO - 1pro msg 2 thread 39296 instance 10320 waiting
2022-03-09 14:47:10,172 INFO - 2pro msg 2 thread 32000 instance 10320 waiting
2022-03-09 14:47:10,173 INFO - 3pro msg 2 thread 69088
2022-03-09 14:47:10,174 INFO - 1con msg 1 thread 46592 instance 10320 waiting
2022-03-09 14:47:10,175 INFO - 2con msg 1 thread 61184 instance 10320 waiting
2022-03-09 14:47:10,175 INFO - 3pro msg 2 thread 53888 instance 10320 waiting
2022-03-09 14:47:10,176 INFO - 3con msg 1 thread 68480 instance 10320 waiting

2022-03-09 14:47:13,175 INFO - 2pro msg 3 thread 69088
2022-03-09 14:47:13,175 INFO - 2pro msg 3 thread 39296 instance 10320 waiting
2022-03-09 14:47:13,176 INFO - 1pro msg 3 thread 69088
2022-03-09 14:47:13,177 INFO - 1pro msg 3 thread 32000 instance 10320 waiting
2022-03-09 14:47:13,177 INFO - 2con msg 2 thread 61184 instance 10320 waiting
2022-03-09 14:47:13,179 INFO - 3pro msg 3 thread 69088
2022-03-09 14:47:13,180 INFO - 1con msg 2 thread 46592 instance 10320 waiting
2022-03-09 14:47:13,180 INFO - 3pro msg 3 thread 53888 instance 10320 waiting
2022-03-09 14:47:13,181 INFO - 3con msg 2 thread 68480 instance 10320 waiting
```