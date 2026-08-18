import * as React from "react"

import { cn } from "@/lib/utils"

function Card({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card"
      className={cn("flex flex-col overflow-hidden bg-card text-card-foreground", className)}
      {...props}
    />
  )
}

function CardImage({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-image"
      className={cn("w-full aspect-video bg-secondary overflow-hidden", className)}
      {...props}
    />
  )
}

function CardHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-header"
      className={cn("pt-4 space-y-1", className)}
      {...props}
    />
  )
}

function CardLabel({ className, ...props }: React.ComponentProps<"p">) {
  return (
    <p
      data-slot="card-label"
      className={cn("text-[10px] tracking-widest uppercase text-muted-foreground", className)}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-title"
      className={cn("text-base font-medium leading-snug", className)}
      {...props}
    />
  )
}

function CardDescription({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-description"
      className={cn("text-sm text-muted-foreground leading-relaxed mt-2", className)}
      {...props}
    />
  )
}

function CardContent({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div data-slot="card-content" className={cn("", className)} {...props} />
  )
}

function CardFooter({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-footer"
      className={cn("pt-4 mt-auto flex items-center", className)}
      {...props}
    />
  )
}

export { Card, CardImage, CardHeader, CardLabel, CardTitle, CardDescription, CardContent, CardFooter }
