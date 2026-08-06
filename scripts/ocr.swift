// OCR a PDF with the macOS Vision framework. Usage: ocr <in.pdf> <out.txt> [dpi]
// Pages are separated by \f to match pdftotext's convention, so downstream page-level
// logic (the reprint-page detector) keeps working.
import Foundation
import PDFKit
import Vision
import CoreGraphics

let args = CommandLine.arguments
guard args.count >= 3 else { FileHandle.standardError.write("usage: ocr in.pdf out.txt [dpi]\n".data(using:.utf8)!); exit(2) }
let inURL = URL(fileURLWithPath: args[1])
let outURL = URL(fileURLWithPath: args[2])
let dpi = args.count > 3 ? (Double(args[3]) ?? 200) : 200
let scale = dpi / 72.0

guard let doc = PDFDocument(url: inURL) else {
    FileHandle.standardError.write("cannot open \(inURL.path)\n".data(using:.utf8)!); exit(1)
}

var out = [String]()
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { out.append(""); continue }
    let rect = page.bounds(for: .mediaBox)
    let w = Int(rect.width * scale), h = Int(rect.height * scale)
    guard w > 0, h > 0,
          let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8,
                              bytesPerRow: 0, space: CGColorSpaceCreateDeviceGray(),
                              bitmapInfo: CGImageAlphaInfo.none.rawValue) else {
        out.append(""); continue
    }
    ctx.setFillColor(CGColor(gray: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: scale, y: scale)
    ctx.translateBy(x: -rect.origin.x, y: -rect.origin.y)
    page.draw(with: .mediaBox, to: ctx)
    guard let img = ctx.makeImage() else { out.append(""); continue }

    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = true
    req.recognitionLanguages = ["en-US"]
    let handler = VNImageRequestHandler(cgImage: img, options: [:])
    do { try handler.perform([req]) } catch { out.append(""); continue }

    // Rebuild reading order: sort by line top, then left edge. CBSE papers are two-column
    // (Hindi | English) so a naive concatenation interleaves the columns.
    let obs = (req.results ?? []).compactMap { $0 as? VNRecognizedTextObservation }
    struct Line { let y: CGFloat; let x: CGFloat; let s: String }
    var lines = [Line]()
    for o in obs {
        guard let c = o.topCandidates(1).first else { continue }
        lines.append(Line(y: 1 - o.boundingBox.maxY, x: o.boundingBox.minX, s: c.string))
    }
    lines.sort { a, b in
        if abs(a.y - b.y) > 0.012 { return a.y < b.y }
        return a.x < b.x
    }
    out.append(lines.map { $0.s }.joined(separator: "\n"))
}
try out.joined(separator: "\u{0C}").write(to: outURL, atomically: true, encoding: .utf8)
