use framework "Foundation"
use framework "AppKit"

on run {query}
    # 获取 NSPasteboard
    set pasteBoard to current application's NSPasteboard's generalPasteboard()
    
    # 保存原始剪贴板内容
    set oldContent to pasteBoard's stringForType:(current application's NSPasteboardTypeString)
    
    # 清空剪贴板并设置新内容
    pasteBoard's clearContents()
    pasteBoard's setString:query forType:(current application's NSPasteboardTypeString)
    
    tell application "System Events"
        key code 0 using {command down}  # Command + A
        key code 123  # 左箭头
        delay 0.02  # 小延迟确保光标已移动
        keystroke "v" using command down
    end tell
    
    # 延迟以确保粘贴完成
    delay 0.04
    
    # 还原原始剪贴板内容
    pasteBoard's clearContents()
    if oldContent is not missing value then
        pasteBoard's setString:oldContent forType:(current application's NSPasteboardTypeString)
    end if
end run