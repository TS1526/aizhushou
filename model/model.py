# 定义大模型的操作方法
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import base64
# 创建Langchain的大模型
def create_model():
    llm = ChatOpenAI(
        # 1、模型的名字
        model="glm-4-0520",
        # 2、api_key
        api_key="4929c0dba7dfb6f4dfec47d8cb0814c4.Impquf9AY64AttYw",
        # 3、温度创新性 0-1
        temperature=0.9,
        # 4、接口的地址
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )
    return llm
# 直接使用大模型进行推理（直接让大模型回答问题）
def model_invoke(message):
    llm = create_model()
    result = llm.invoke(message)
    return result.content

def create_fanyi_prompt_chain():
    prop = PromptTemplate(
        input_variables=["context"],
        template="""
           你是一个翻译官，只能翻译问题。用户输入的问题是：{context}
        """
    )
    llm = create_model()
    chain = prop | llm
    return chain
# 通过langchain链实现结果的调用
def chain_invoke(message):
    chain = create_fanyi_prompt_chain()
    result = chain.invoke(message)
    return result.content