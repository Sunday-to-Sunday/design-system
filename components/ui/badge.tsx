import { mergeProps } from "@base-ui/react/merge-props"
import { useRender } from "@base-ui/react/use-render"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex w-fit shrink-0 items-center justify-center gap-1 whitespace-nowrap text-[10px] tracking-widest uppercase font-medium transition-all [&>svg]:pointer-events-none [&>svg]:size-3",
  {
    variants: {
      variant: {
        // Primary — dark fill, white text (like "FAMILY AND FRENS CONDITION")
        default:
          "bg-foreground text-background px-3 py-1",
        // Outline — bordered, no fill
        outline:
          "border border-foreground text-foreground px-3 py-1",
        // Muted — light surface
        secondary:
          "bg-secondary text-secondary-foreground px-3 py-1",
        // Destructive
        destructive:
          "bg-destructive text-background px-3 py-1",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

function Badge({
  className,
  variant = "default",
  render,
  ...props
}: useRender.ComponentProps<"span"> & VariantProps<typeof badgeVariants>) {
  return useRender({
    defaultTagName: "span",
    props: mergeProps<"span">(
      { className: cn(badgeVariants({ variant }), className) },
      props
    ),
    render,
    state: { slot: "badge", variant },
  })
}

export { Badge, badgeVariants }
