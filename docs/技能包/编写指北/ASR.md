ASR的main函数也有一个参数：file

file表示音频文件路径

另外，ASR的main函数需要在最后加上这一句话：

比如，识别好的文字是cg

```python
model.func.run(cg)  # 调用技能
```

除此之外，无特别强调。