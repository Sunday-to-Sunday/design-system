import * as React from "react"
import { Input as InputPrimitive } from "@base-ui/react/input"

import { cn } from "@/lib/utils"

function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return (
    <InputPrimitive
      type={type}
      data-slot="input"
      className={cn(
        "h-10 w-full min-w-0 border-0 border-b border-border bg-transparent px-0 py-2 text-sm text-foreground transition-colors outline-none",
        "placeholder:text-muted-foreground/60",
        "focus-visible:border-foreground focus-visible:ring-0",
        "disabled:pointer-events-none disabled:opacity-40",
        "aria-invalid:border-destructive",
        className
      )}
      {...props}
    />
  )
}

export { Input }
