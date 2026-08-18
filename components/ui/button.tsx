import { Button as ButtonPrimitive } from "@base-ui/react/button"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex shrink-0 items-center justify-center whitespace-nowrap transition-all outline-none select-none disabled:pointer-events-none disabled:opacity-40 [&_svg]:pointer-events-none [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        // Primary — text + underline, used with ↗ arrow
        default:
          "gap-1.5 border-b border-foreground text-foreground font-light pb-0.5 hover:opacity-50",
        // Solid — black fill, uppercase, for high-emphasis CTAs
        solid:
          "gap-2 px-8 py-3 bg-foreground text-background text-[10px] tracking-widest uppercase hover:opacity-80",
        // Outline — bordered, no fill
        outline:
          "gap-2 px-6 py-2.5 border border-border text-foreground text-[10px] tracking-widest uppercase hover:border-foreground",
        // Ghost — plain text, no decoration
        ghost:
          "gap-1.5 text-foreground hover:text-muted-foreground",
        // Destructive — underline red
        destructive:
          "gap-1.5 border-b border-destructive text-destructive pb-0.5 hover:opacity-50",
        // Secondary — muted surface fill
        secondary:
          "gap-2 px-6 py-2.5 bg-secondary text-secondary-foreground text-[10px] tracking-widest uppercase hover:bg-accent",
      },
      size: {
        sm: "text-xs",
        default: "text-sm",
        lg: "text-base",
        icon: "size-9 justify-center",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  ...props
}: ButtonPrimitive.Props & VariantProps<typeof buttonVariants>) {
  return (
    <ButtonPrimitive
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  )
}

export { Button, buttonVariants }
