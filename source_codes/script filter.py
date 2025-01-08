#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys

def get_items():
    """Return the list of all prompt items with separate search keys"""
    return [
        {
            "title": "🔠⇨🔠 polish",
            "subtitle": "英文学术写作润色",
            "arg": "Below is a paragraph from an academic paper. Polish the writing to meet the academic style, improve the spelling, grammar, clarity, concision and overall readability. Only replace the word and rewrite the whole sentence when necessary. The writing should follow academic style and do not use words that are too fancy:\n\n",
            "search_keys": ["polish"],
            "icon": {
                "type": "fileicon",
                "path": "/System/Applications/TextEdit.app"
            }
        },

        {
            "title": "📚加入Bibtex",
            "subtitle": "加入bibtex引用",
            "arg": "按照上文已有的bibtex的格式，加入下面的citation。注意和上文已有的bibtex保持一样的缩写、格式等。尤其注意对arxiv文章的引用（应类似于@article{arxiv'22:adatask,\n  title   = {AdaTask: Adaptive Multitask Online Learning},\n  author  = {Laforgue, Pierre and Della Vecchia, Andrea and Cesa-Bianchi, Nicol{\`o} and Rosasco, Lorenzo},\n  journal = {ArXiv preprint},\n  volume  = {arXiv:2205.15802},\n  year    = {2021}\n}）：\n\n",
            "search_keys": ["bibtex"],
            "icon": {
                "type": "fileicon",
                "path": "/System/Applications/Notes.app"
            }
        },
        {
            "title": "🔠⇨🀄️ 英译中",
            "subtitle": "学术翻译 英译中",
            "arg": "你是一位科研论文审稿员，擅长写作高质量的科研论文，尤其是机器学习和人工智能领域的论文。\n请你帮我准确且学术性地将以下源文本翻译成流畅、易于阅读的中文，且将数学公式翻译为$符号包裹的LaTeX代码。在翻译专有术语时，请总是使用括号额外标注出该术语的原文。请直接输出翻译后的文本。\n\n源文本:",
            "search_keys": ["yingyizhong"],
            "icon": {
                "type": "fileicon",
                "path": "/System/Applications/Font Book.app"
            }
        },
        {
            "title": "🀄️⇨🔠 中译英",
            "subtitle": "学术翻译 中译英",
            "arg": "Please translate following sentence to English with academic writing, improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence.\n\n",
            "search_keys": ["zhongyiying"],
            "icon": {
                "type": "fileicon",
                "path": "/System/Applications/Font Book.app"
            }
        },
        {
            "title": "🀄️⇨🀄️ 中文 polish",
            "subtitle": "学术写作润色（详细修改说明）",
            "arg": "作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本：\n\n",
            "search_keys": ["polishzhong"],
            "icon": {
                "type": "fileicon",
                "path": "/System/Applications/TextEdit.app"
            }
        },
        {
            "title": "✍🏻 解释每步代码的作用",
            "subtitle": "解释代码",
            "arg": "I would like you to serve as a code interpreter with Chinese, and elucidate the syntax and the semantics of the code line-by-line:\n\n",
            "search_keys": ["jieshi", "code", "python"]
        }
    ]

def calculate_relevance(item, query):
    """计算项目与搜索词的相关度分数"""
    score = 0
    
    # 检查搜索关键词
    for key in item['search_keys']:
        if query in key.lower():
            # 如果搜索词在开头，给予更高分数
            if key.lower().startswith(query):
                score += 3
            else:
                score += 1
                
    # 检查标题和副标题
    if query in item['title'].lower():
        if item['title'].lower().startswith(query):
            score += 2
        else:
            score += 1
            
    if query in item['subtitle'].lower():
        if item['subtitle'].lower().startswith(query):
            score += 2
        else:
            score += 1
            
    return score

def search_items(query):
    """Filter items based on search query"""
    items = get_items()
    
    # If no query or empty query, return all items sorted by title
    if not query or query == '':
        return items
    
    # Convert query to lowercase for case-insensitive search
    query = query.lower().strip()
    
    # Filter and score items
    scored_items = []
    for item in items:
        score = calculate_relevance(item, query)
        if score > 0:
            scored_items.append((score, item))
    
    # Sort by score in descending order
    scored_items.sort(key=lambda x: x[0], reverse=True)
    
    # Return only the items, without scores
    return [item for score, item in scored_items]

def main():
    try:
        # Get query from Alfred
        query = sys.argv[1] if len(sys.argv) > 1 else ""
        
        # Get filtered items
        items = search_items(query)
        
        # Prepare output for Alfred
        output = {"items": items}
        
        # Print JSON output
        print(json.dumps(output, ensure_ascii=False))
    except Exception as e:
        # Error handling
        error_output = {
            "items": [{
                "title": "Error occurred",
                "subtitle": str(e),
                "arg": ""
            }]
        }
        print(json.dumps(error_output, ensure_ascii=False))

if __name__ == "__main__":
    main()