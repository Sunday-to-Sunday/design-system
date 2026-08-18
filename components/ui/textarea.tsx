import * as React from "react"

import { cn } from "@/lib/utils"

function Textarea({ className, ...props }: React.ComponentProps<"textarea">) {
  return (
    <textarea
      data-slot="textarea"
      className={cn(
        "w-full min-h-[60px] border-0 border-b border-border bg-transparent px-0 py-2 text-sm text-foreground transition-colors outline-none resize-none",
        "placeholder:text-muted-foreground/60",
        "focus-visible:border-foreground focus-visible:ring-0",
        "disabled:cursor-not-allowed disabled:opacity-40",
        "aria-invalid:border-destructive",
        className
      )}
      {...props}
    />
  )
}

export { Textarea }
